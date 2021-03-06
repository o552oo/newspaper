from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать, и фильтры потеряются

@register.filter(name='Censor')  # регистрируем наш фильтр под именем Censor, чтоб django понимал, что это именно фильтр, а не простая функция
def cut(value, arg):  # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|cut:arg
    return value.replace(arg, '')  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон