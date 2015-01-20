from django.shortcuts import render


def home_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        
        home_html_file = open('templates/home.html', 'r')
        home_html_text = home_html_file.read()
        home_html_file.close()
        
        with open('templates/home.html', 'w') as new_home:
            if email in home_html_text:
                new_home.write(home_html_text.replace(''.join(['      <p>', email, '</p>\n']), ''))
            else:
                new_home.write(home_html_text.replace('<div id="emails">\n', ''.join(['<div id="emails">\n      <p>', email, '</p>\n'])))
    
    return render(request, 'home.html')

