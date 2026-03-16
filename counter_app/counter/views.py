from django.shortcuts import render

def counter_view(request):
    count = request.session.get('count', 0)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increment':
            count += 1
        elif action == 'decrement':
            count -= 1
        elif action == 'reset':
            count = 0
        request.session['count'] = count

    return render(request, 'counter/index.html', {'count': count})