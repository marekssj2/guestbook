from django.shortcuts import render
from .models import Comment
from .forms import CommentForm

# Create your views here.

def index(request):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            botcather = form.cleaned_data['botcather']
            if not botcather:
                new_comment = Comment(name=name, comment=comment)
                new_comment.save()

        
#    else:
    form = CommentForm()

    comments = Comment.objects.order_by('-date_added')
    context = {'comments' : comments, 'form' : form}
    return render(request, "guestApp/index.html", context)