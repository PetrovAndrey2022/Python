


a=123
b=1.23
c='Привет'


print(a,b,c)
# Интерполящия строк
print(f'a=',{a},'b=',{b},'c=',{c}) # a= {123} b= {1.23} c= {'Привет'}  
print(a,'-',b,'-',c) # 123 - 1.23 - Привет
print('{}-{}-{}'.format(a,b,c)) # 123-1.23-Привет
print('{2}-{1}-{0}'.format(a,b,c)) # Привет-1.23-123