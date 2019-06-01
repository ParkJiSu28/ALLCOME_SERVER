from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizRequestViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        subject = self.request.query_params.get('subject', None)
        if subject is not None:
            subject_qs = qs.filter(subject=subject)
            return subject_qs.order_by("?")[:1]


class MockTestViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        subject = self.request.query_params.getlist('subject', None)
        print(subject)
        print(len(subject))

        if len(subject) == 1:
            subject_qs = qs.filter(subject=subject.pop())
            return subject_qs.order_by("?")[:1]

        if len(subject) == 2:
            subject_qs_1 = qs.filter(subject=subject.pop())
            subject_qs_2 = qs.filter(subject=subject.pop())
            first = subject_qs_1.order_by("?")[:10]
            second = subject_qs_2.order_by("?")[:10]
            res = first | second
            return res

        if len(subject) == 3:
            subject_qs_1 = qs.filter(subject=subject.pop())
            subject_qs_2 = qs.filter(subject=subject.pop())
            subject_qs_3 = qs.filter(subject=subject.pop())
            first = subject_qs_1.order_by("?")[:7]
            second = subject_qs_2.order_by("?")[:7]
            third = subject_qs_3.order_by("?")[:8]
            res = first | second | third
            return res

        if len(subject) == 4:
            subject_qs_1 = qs.filter(subject=subject.pop())
            subject_qs_2 = qs.filter(subject=subject.pop())
            subject_qs_3 = qs.filter(subject=subject.pop())
            subject_qs_4 = qs.filter(subject=subject.pop())
            first = subject_qs_1.order_by("?")[:5]
            second = subject_qs_2.order_by("?")[:5]
            third = subject_qs_3.order_by("?")[:5]
            fourth = subject_qs_4.order_by("?")[:5]
            res = first | second | third | fourth
            return res

        if len(subject) == 5:
            subject_qs_1 = qs.filter(subject=subject.pop())
            subject_qs_2 = qs.filter(subject=subject.pop())
            subject_qs_3 = qs.filter(subject=subject.pop())
            subject_qs_4 = qs.filter(subject=subject.pop())
            subject_qs_5 = qs.filter(subject=subject.pop())
            first = subject_qs_1.order_by("?")[:6]
            second = subject_qs_2.order_by("?")[:6]
            third = subject_qs_3.order_by("?")[:6]
            fourth = subject_qs_4.order_by("?")[:6]
            fifth = subject_qs_5.order_by("?")[:6]
            res = first | second | third | fourth | fifth
            return res

        if len(subject) == 6:
            subject_qs_1 = qs.filter(subject=subject.pop())
            subject_qs_2 = qs.filter(subject=subject.pop())
            subject_qs_3 = qs.filter(subject=subject.pop())
            subject_qs_4 = qs.filter(subject=subject.pop())
            subject_qs_5 = qs.filter(subject=subject.pop())
            subject_qs_6 = qs.filter(subject=subject.pop())
            first = subject_qs_1.order_by("?")[:5]
            second = subject_qs_2.order_by("?")[:5]
            third = subject_qs_3.order_by("?")[:5]
            fourth = subject_qs_4.order_by("?")[:5]
            fifth = subject_qs_5.order_by("?")[:5]
            sixth = subject_qs_6.order_by("?")[:5]
            res = first | second | third | fourth | fifth | sixth
            return res

        if len(subject) == 7:
            subject_qs_1 = qs.filter(subject=subject.pop())
            subject_qs_2 = qs.filter(subject=subject.pop())
            subject_qs_3 = qs.filter(subject=subject.pop())
            subject_qs_4 = qs.filter(subject=subject.pop())
            subject_qs_5 = qs.filter(subject=subject.pop())
            subject_qs_6 = qs.filter(subject=subject.pop())
            subject_qs_7 = qs.filter(subject=subject.pop())
            first = subject_qs_1.order_by("?")[:4]
            second = subject_qs_2.order_by("?")[:4]
            third = subject_qs_3.order_by("?")[:4]
            fourth = subject_qs_4.order_by("?")[:4]
            fifth = subject_qs_5.order_by("?")[:4]
            sixth = subject_qs_6.order_by("?")[:5]
            seventh = subject_qs_7.order_by("?")[:5]
            res = first | second | third | fourth | fifth | sixth | seventh
            return res


@api_view(['GET'])
def subject_view(request):
    data = [
        {"subject1": "Algorithme"},
        {'subject2': 'Database'},
        {'subject3': 'Software_Engineering'},
        {'subject4': 'operation_system'},
        {'subject5': 'computer_network'},
        {'subject6': 'computer_structure'},
        {'subject7': 'Data_structure'},
    ]
    return Response(data=data)
