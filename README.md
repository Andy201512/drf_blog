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

database table 'tags' design:
| fileds | types |
| :---: | :---: |
| name | CharField|

database table 'blog' design:
| fileds | types |
| :---: | :---: |
| title | CharField |
| author | ForeignKey |
| create_time | DateTimeField |
| modify_time | DateTimeField |
| excerpt | TextField |
| category |  ManyToManyField |
| tags | ManyToManyField |
| views | PositiveIntegerField |
| body | TextField |
### Views and Urls
### Pages
