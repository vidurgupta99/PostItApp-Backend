from rest_framework.response import Response
from .models import PostIt
from .serializers import PostItSerializer

# API Routes

# Create
def createPostIt(request):
    serializer = PostItSerializer(postit, many=False)
    data = request.data
    postit = PostIt.objects.create(
        body=data['body']
    )
    return Response(serializer.data)

# Read
def getPostIts(request):
    serializer = PostItSerializer(postits, many=True)
    postits = PostIt.objects.all().order_by('-updated')
    return Response(serializer.data)


def getPostItInfo(request, pk):
    serializer = PostItSerializer(postits, many=False)
    postits = PostIt.objects.get(id=pk)
    return Response(serializer.data)

# Update
def updatePostIt(request, pk):
    serializer = PostItSerializer(instance=postit, data=data)
    data = request.data
    postit = PostIt.objects.get(id=pk)

    if serializer.is_valid():
        serializer.save()

    return serializer.data

# Delete
def deletePostIt(request, pk):
    postit = PostIt.objects.get(id=pk)
    postit.delete()
