# drf_blog  
a Django REST framework blog

## env
python 3.6  
django 3.1.2  
djangorestframework 3.11.2  
### warnning
before using this blog in production environmentt, remember to change the website SECRET_KEY in `drf_blog/website/website/setting.py`

## source code
blog source codes and website setting

### Modles
database table 'category' design: 
| fileds | types |
| :---: | :---: |
| name | CharField|

database table 'tag' design:
| fileds | types |
| :---: | :---: |
| name | CharField|

database table 'blog' design:
| fileds | types |
| :---: | :---: |
| title | CharField |
| author | ForeignKey |
| created_time | DateTimeField |
| modifyed_time | DateTimeField |
| excerpt | TextField |
| category |  ForeignKey |
| tags | ManyToManyField |
| views | PositiveIntegerField |
| img | ImageField |
| body | TextField |
###  drf viewsets 
serializer: default  
pagenation: page_size = 5  
permission: IsAuthenticateOrReadOnly, IsAuthorOrReadOnly  
### Pages
