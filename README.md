# nara
Create a web application where there are three entities - Company, Article, Users and Roles.
Company has many Articles. User has and belongs to many Companies through Roles table.
On an admin Portal, we should be able to give user specific access to Company and Articles.
Accesses are like this.
A User can be an ADMIN of Company. He can see and edit all the articles that belongs to the company.
A User can be a MEMBER of a Company. The user can see the Articles, but cannot edit it.
If a User is a MEMBER of a Company, he can be given ADMIN access to an Article, which will let him to edit the Article.
A User with no access in Company shouldn’t see the articles.

Use Casbin for Authorisation Roles.

Code Quality is of prime importance and you will be accessed for
1. Solutions
2. Code quality
3. Modularity of code
4. Use micro-services pattern (Deploy Casbin as a separate service)
5. Use python for your application development

Build using Dockerfile in Github Actions or manually and push to AWS ECR. (Github Actions a plus).
Deploy Casbin and python application on Fargate in AWS.
