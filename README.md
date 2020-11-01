# drf_blog  
a Django REST framework blog

## env
python 3.6  
django 3.1.2  
djangorestframework 3.11.2

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
### Views
### Pages
