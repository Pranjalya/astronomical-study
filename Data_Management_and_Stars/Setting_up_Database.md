## Setting up a Database

#### Cons of Flat File Storage
- Firstly, it's hard to manage data redundancy and inconsistency.
- Secondly, depending on the format, the data can only be accessed with custom software. In other words, all queries and filters have to be pre-implemented. 
- Thirdly, in large projects, you may need to restrict access to parts of the day to some of the researchers
within the collaboration which then leads to security problems.

### Databases

- Database systems insure atomicity, either the transaction occurred or it didn't. 
- For databases to do all this, they have to be able to retrieve data efficiently. This requires complex data structures, but the whole point is that the database is doing this for you. 
- So when we think about databases, we're thinking about abstraction.

##### Layers of Database

- __Physical Layer__
    -  How the data is actually stored and
indexed on the computer
- __Logical Layer__
    - This is where we think about what data is stored in the database and how those data are organised, and indexed.
    - We can find out this information through the published schema.
- __View Layer__
    - It is just a view of the database for
a particular purpose. 

##### Steps
1. Data Collection
    - We'll start with data from the hypothos catalog.
Hypothos was a scientific satellite that measured the power lapses of stars for the purposes of knowing how far away they were.
    - It also measured their brightnesses and their colors.
    - We'll combine hypothos data with cluster membership list from bazeer, which gave the probability of each star being physically associated with that cluster. 
2. Decide DBMS
    - Some of the common platforms are SQL Server, MySQL and PostgreSQL or Postgres.
    - For this course, we'll use Postgres, because it's a widely used, free open source DBMS with support for spatial queries.
3. Design Schema
    - The schema sets out the attributes of each table in your database and how the tables relate to each other.
    - It lists the type of and constraints on the attributes in each table, and identifies the primary key for each table which ensures that each row has a unique key.
    - It also describes the relationship between the tables.