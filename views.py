from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .migrations.utils import process_orders
from .serializers.serializers import SolutionSerializer


@api_view(['POST'])
def process_solution(request):
    try:
        serializer = SolutionSerializer(data=request.data)

        if serializer.is_valid():
            orders = serializer.validated_data.get('orders', [])
            criterion = serializer.validated_data.get('criterion', 'all')

            if not orders:
                return Response({"error": "La lista de pedidos está vacía."}, status=status.HTTP_400_BAD_REQUEST)

            result = process_orders(orders, criterion)

            return Response({"result": result}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
