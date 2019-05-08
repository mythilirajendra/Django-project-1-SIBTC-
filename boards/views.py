from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import NewTopicForm
from django.http import HttpResponse
from .models import Board, Topic, Post
def home(request):
    boards= Board.objects.all()
    return render(request,'home.html',{'boards':boards})


def board_topics(request,pk):
    board= get_object_or_404(Board,pk=pk)

    
    return render(request,'topics.html',{'board':board})

def new_topic(request,pk):
    board= get_object_or_404(Board,pk=pk)
    user=User.objects.first()
    if request.method=='POST':
        form=NewTopicForm(request.POST)
        if form.is_valid():
            topic= form.save(commit=False)
            topic.board= board
            topic.starter= user
            topic.save()
            post= Post.objects.create(message=form.cleaned_data.get('message'), topic=topic, created_by=user)
            return redirect('board_topics',pk=board.pk)
    else:
        form= NewTopicForm()
    return render(request,'new_topic.html',{'board':board,'form':form})
        #subject=request.POST['subject']
        #message=request.POST['message']
        
        #topic=Topic.objects.create(subject=subject,board=board,starter=user)
        #post=Post.objects.create(message=message,topic=topic,created_by=user)
        #return redirect('board_topics', pk=board.pk)
    #return render(request,'new_topic.html',{'board':board})


	#boards_name= list()
	#for board in boards:

		#boards_name.append(board.name)
	#response_html='<br>'.join(boards_name)
    
    #return HttpResponse(response_html)
    
    #return render(request,'home.html',{'boards':boards})

	