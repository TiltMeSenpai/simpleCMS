<p>
Now that we have our injection point, it's time to see what we can get our database to do for us. While we always could just use a tool like SQLMap at this point, the whole aim of this series is to learn the types of queries that SQLMap actually uses to accomplish what it does.
</p>
<p>From here, our next steps will be to figure out what type of database our system is running, map out the layout of the databases we are interested in, and dump as much information as we can.
</p>
<h2>Basic Database Fingerprinting</h2>
<p>
There's been quite a few articles on this subject, so I'm not going to go too much into depth, but it's worth covering the basics.
</p>
<ol>
    <li>Comment Delimiters:<br/>
        Because comments are often used to discard the later parts of the query that we aren't interested in, finding comment characters will most likely be one of the first steps in SQLi fingerprinting anyways
        <ul>
            <li>
                "#":
                <ul>
                    <li>PostgreSQL</li>
                    <li>MySQL (<em>NOTE: Since MySQL and PostgreSQL both support "#" and "--" as single line comments, but the SQL standard is the "--" sequence, testing with "#" will allow you to actually fingerprint the database</em>)</li>
                </ul>
            </li>
            <li>
                "--":
                <ul>
                    <li>Oracle</li>
                    <li>MsSQL</li>
                    <li>SQLite</li>
                    <li>...</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Version Numbers:<br/>
        I believe the standard way to find the SQL version is the @@VERSION query, but I'm truthfully not sure. The two that seem to work are either @@VERSION or VERSION()
        <ul>
            <li>5.x.x: MySQL</li>
            <li>9.x.x or 8.x.x: PostgreSQL</li>
            <li>8-12.x.xxxx: MsSQL (<em>Note: This intersects with the PostgreSQL versions, but only PostgreSQL accepts "#" as a comment</em>)
            <li>None of those seem to work?
                <ul>
                    <li>Using v$instance, 10.x.x.x.x or 11.x.x.x.x</li>
                    <li>Still can't find it: Might be SQLite or something that I havent seen before. Good luck.</li>
                </ul>
            </li>
        </ul>
    </li>
</ol>
<p> It's important to note that this is very far from a complete list. There's way to many implementations of SQL databases, and they all have their quirks and stuff, but as far as I know, these are the more common systems.
</p>
<h2> Starting the strange stuff </h2>
<p>
    From here on out, we're just going to assume that we have a MySQL database at our hands. Out of everything, it's the most common for personal projects, and it has the most support for the strange queries that we need. And anyways, this is supposed to be an informative post, not a guide to hacking everything.
</p>
<h3> The UNION verb </h3>
<p>
    In the case of exploiting string-based SQLi's (The easiest type), the UNION query is close to your most valuable verb. It takes 2 SELECT statements (With the same number of columns) and concatenates the results together. However, it does require the two selects to have the same number of columns, and in most cases, we can't control the number of columns selected in our first statement.
</p>
<h4> Adding and removing columns </h4>
<p>
    Removing columns is the easy part. Instead of using "SELECT a, b FROM table", we can use "SELECT a FROM table" to match columns. However, when the first SELECT statement contains 3 columns, and our target table only has 2 colums, our statements get a little more obscure.
</p>
<h4> Selecting data </h4>
<p>
    Thankfully, (at least for MySQL), you can select a constant instead of a column from a table. (I.E, SELECT 'a'; is a perfectly valid statement). Therefore, if we need 3 columns, but our target table has only 2, we can use "SELECT a, b, 'c' FROM table" for our select. Now, (Finally) we can get back to our phonebook again.
</p>
<h2> Exploitation </h2>
<p>
    Recall that our target query is
    <pre class="prettyprint lang-sql">
        Conn.query("SELECT name, number FROM phonebook WHERE name LIKE '"+name+"';")
    </pre>
    In order to properly fingerprint our database, we still need the version number. However, the version is only one column, and we need 2 columns. Therefore, we need to select constants in order to pad out our injected query to the required number of columns. Because of this, our input should look something like:
    <pre class="prettyprint lang-sql">
        trash' UNION SELECT @@version, 'a
    </pre>
    transforming our query into
    <pre class='prettyprint lang-sql'>
        SELECT name, number FROM phonebook WHERE name LIKE 'trash' UNION SELECT @@version, 'a';
    </pre>
    <em> Note: Here, we didn't actually use a comment character. In some cases, it's possible to craft your injection to line up with the original query</em><br/>
    Our output will look something like:
    <pre>
        <table>
            <tr><td>Name</td><td>Number</td></tr>
            <tr><td>5.5.32  </td>  <td>a</td></tr>
        </table>
    </pre>
</p>
<h2> Information Schema: Your Best Friend </h2>
<p>
    Now we know the type of database we are dealing with, but we still know nothing about the internal layout of the database. However, most database systems (MySQL included) contain an awesome database called "information_schema" that stores metadata for the server itself. Luckily, it contains quite a bit of information we want, such as table names, and the collumns of our tables. All of the following data can be easily extracted using UNION SELECT's
    <h3> Finding a table </h3>
    <p>Information about the tables in our database server is stored in a table called "information_schema.tables". While this table also stores metadata for system tables, filtering that out is fairly trivial. The query we want is:
    <pre class='prettyprint lang-sql'>
    SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA NOT LIKE "information_schemaj;
    </pre>
    Information_schema.tables actually stores quite a bit more metadata than this, but the table name is honestly the only useful thing for us in this table.</p>
    <h3> Finding Columns </h3>
    <p>Similar to tables, information about columns is stored in a table called "information_schema.columns". This table also contains quite a bit of useless data and system tables, but once again, that is easily filtered out. Our query in this case would be:
    <pre class="prettyprint lang-sql">
    SELECT DATA_TYPE, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME LIKE '*our table*';
    </pre>
    Naturally, you should probably replace *our table* with the name of the table you actually want.
    </p>
</p>
Now, this database is all ours. We can use UNION SELECT statements to extract whatever data we feel like. For example, if our phonebook also had user account in order to modify or claim entries, we could extract passwords and such from the user table and hijack user accounts.
