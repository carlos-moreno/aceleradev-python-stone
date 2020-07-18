from collections import Counter
from itertools import repeat, chain

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def lambda_function(request):
    try:
        data = request.data['question']
        solution = list(chain.from_iterable(repeat(k, v)
                                            for k, v in Counter(data).most_common()))
        return Response({"solution": solution})
    except KeyError:
        return Response(
            {'detail': 'Invalid request, a JSON containing the question key and a list '
                       'is expected. e.g. {"question": [2, 3, 3, 3, 2]}'},
            status=status.HTTP_400_BAD_REQUEST
        )
