import http.client

from django import forms


class PageAnalyserForm(forms.Form):
    
    """ Problem: url needs to have 'http://' to be valid, but the HTTPSConnection
    method is interpreting 'http' as a port number because of the colon. Changed to
    char field as workaround"""
    
    url = forms.CharField(
        required=True,
        label='URL',
    )
    
    def analyse_page(url):
        connection = http.client.HTTPSConnection(url)
        connection.request('GET', '/')
        response = connection.getresponse()
        data = response.read()
        print(data)