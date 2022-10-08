**Case**

Database storing songs liked by users. Since this is used for a recommender system, a lot of additional information
will need to be stored. It is also assumed that the number of entries will increase rapidly (when liking a song). 
With a large number of users, suppose the need for a distributed database.
It looks like using a SQL data storage would be a good solution.

Structure:

<img src="https://github.com/Yuki-53/web_python/blob/hw_4/imgs/database.jpg"/>

**Oracle Database**

Popular with developers, clear documentation, support for long names, JSON, improved list tag, and Oracle Cloud.

Advantages:
- Large capacity
- SQL support

Disadvantages:
- High cost
- The need for a strong infrastructure

**MySQL**

This database management system uses a standard form of SQL. MySQL supports up to 50 million rows per table.
Supports partitioning and replication, as well as Xpath and stored procedures, triggers.

Advantages:
- Simplicity
- Lots of features
- Safety
- Speed

Disadvantages:
- Some functionality limitations
- Reliability Issues
- Stagnation in development

**PostgreSQL**

Scalable object-relational database. There are features such as logical replication, declarative table partitioning,
improved parallel queries, more secure password authentication based on SCRAM-SHA-256.

Advantages:
- Full SQL compatibility
- Community
- Third party support
- Expandability
- Object-oriented

Disadvantages:
- Performance
- Сomplexity

**Conclusion**

To me it looks like MySQL is a good choice, it has scalability issues, but in this case it is better than others because 
of its simplicity, other solutions are too powerful or slow for this task
