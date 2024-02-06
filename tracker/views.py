

from django.shortcuts import render, redirect

from tracker import models
# Create your views here.

# View functions must always have request as their first parameter.
def hello_world(request):
    return render(request, "tracker/hello_world.html")

def todo(request):
    # Query a list of all assignments
    assignments = models.Assignment.objects.all()

    context = {
        "assignments": assignments,
    }

    return render(request, "tracker/todo.html", context)

def add_assignment(request):
    context = {

    }

    # In a view like this there are two possibilities:
    # - The browser is loading the form; or [GET method]
    # - The browser is submitting the form. [POST method]

    if request.method == 'POST':
        # The client is submitting the form: add an assignment
        title = request.POST.get('title', None) # return the 'title' of the request, or
                                                # None if not provided
        description = request.POST.get('description', None)

        if title is not None and description is not None:
            new_assignment = models.Assignment(
                course=models.Course.objects.last(),
                title=title,
                description=description,
                points=100,
            )
            new_assignment.save()

            return redirect('todo')

    return render(request, "tracker/add_assignment.html", context)

