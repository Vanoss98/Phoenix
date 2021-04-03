from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
@register.filter()

def custom_dates(string1):

    lookp_dict = {"Farvardin":"فروردین", "Ordibehesht":"اردیبهشت",
     "Khordad":"خرداد", "Tir":"تیر", "Mordad":"مرداد", "Shahrivar":"شهریور",
     "Mehr":"مهر", "Aban":"آبان", "Azar":"آذر", "Dey":"دی", "Bahman":"بهمن", "Esfand":"اسفند"} 
    temp = string1.split() 
    res = [] 
    for wrd in temp: 
        res.append(lookp_dict.get(wrd, wrd)) 
    res = ' '.join(res) 
    return(res)
  

