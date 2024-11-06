import graphene 
from graphene_django import DjangoObjectType 
from graphene_django.filter import DjangoFilterConnectionField 
from graphql import GraphQLResolveInfo, GraphQLError 
from orders.models import Order, OrderLesson 
from lessons.models import Lesson 

class LessonObjectType(DjangoObjectType): 
    class Meta: 
        model = Lesson 
        filter_fields = ('id', 'topic', 'cash') 
        interfaces = (graphene.relay.Node,) 
        decoded_id = graphene.ID() 
        def resolve_decoded_id(self, info): 
            return self.id 
        
class OrderLessonObjectType(DjangoObjectType): 
    lesson = graphene.Field(LessonObjectType) 
    class Meta: model = OrderLesson 
    filter_fields = ('lesson', 'quantity', 'price') 
    
class OrderObjectType(DjangoObjectType): 
    order_lessons = graphene.List(OrderLessonObjectType) 
    def resolve_order_lessons(self, info): 
        return self.order_lessons.all() 
    class Meta: 
        model = Order 
        fields = ('uuid', 'user', 'total_price', 'created_at', 'updated_at', 'order_lessons') 
        
class Query(graphene.ObjectType): 
    hello = graphene.String(default_value="Hi!") 
    lessons = DjangoFilterConnectionField(LessonObjectType) 
    orders = graphene.List(OrderObjectType) 
    def resolve_orders(self, info: GraphQLResolveInfo): 
        queryset = Order.objects.all() 
        fields = info.field_nodes[0].selection_set.selections 
        for field in fields: 
            if field.name.value == 'order_lessons': 
                queryset = queryset.prefetch_related('order_lessons') 
                nested_fields = field.selection_set.selections 
                for nested_field in nested_fields: 
                    if nested_field.name.value == 'lesson': queryset = queryset.prefetch_related('order_lessons__lesson') 
                    break 
                break 
            return queryset 

class CreateOrderLessonInput(graphene.InputObjectType): 
    lesson_id = graphene.ID() 
    quantity = graphene.Decimal() 
    
class CreateOrder(graphene.Mutation): 
    class Arguments: 
        order_lessons = graphene.List(CreateOrderLessonInput) 
    order = graphene.Field(OrderObjectType) 
    
    def mutate(self, info, order_lessons): 
        user = info.context.user 
        if not user.is_authenticated: 
            raise GraphQLError('You must be authenticated to create an order') 
        lessons = Lesson.objects.in_bulk([op.lesson_id for op in order_lessons]) 
        if len(lessons) != len(order_lessons): 
            raise GraphQLError('Some lessons do not exist') 
        order = Order.objects.create(user=info.context.user) 
        order_lessons_instances = [ 
            OrderLesson(order=order, lesson=lessons[int(op.lesson_id)], 
                        quantity=op.quantity, price=lessons[int(op.lesson_id)].cash * op.quantity) 
            for op in order_lessons] 
        OrderLesson.objects.bulk_create(order_lessons_instances) 
        order.update_total_price() 
        order = Order.objects.prefetch_related('order_lessons__lesson').get(pk=order.pk) 
        return CreateOrder(order=order) 

class Mutation(graphene.ObjectType): 
    create_order = CreateOrder.Field() 
    
schema = graphene.Schema(query=Query, mutation=Mutation)