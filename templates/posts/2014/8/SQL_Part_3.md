Numeric SQL Inection
---

Well, now we've hopefully been successful with removing all instances of string
based SQL injection. However, is this our only injection vector? Unfortunately,
far from it.


In edge cases, such as numeric parameters (Think page id's, like
Drupal), programmers will forget to escape the id parameter because they don't
realize that this can also be an injection vector. However, in some ways, this
can be easier to exploit than our previous example.


Let's try and exploit a reverse phone number lookup feature.  
*Note: This uses the same schema as the previous posts.*

```SQL
SELECT id, name, number FROM phonebook WHERE id = <input 1>
```


Now, with all of our string-based vectors already patched, we can no longer
exploit the first input. However, the second input is still vulnerable to
injection. Notice that if we input "abc" for input 1, we get a 500 error, stating
"Undeclared variable: abc: SELECT * FROM phonebook LIMIT abc". However, exploiting
this vulnerability is a little more tricky than string based injection. Because
our injection point is inside a LIMIT statement (and the point of this article
isn't to demonstrate UNION or stacked queries), we can't simply dump our results
as text.


Begin The Exploitation
---

Notice that if we input "1+1" in the second field, the result is the same as
inputing "2". Similarly, notice that inputing "2-1" returns the same result as
inputing "1". So, this demonstrates that at the least, we can execute basic math
within the query, but this is a long shot from exfiltrating data.


However, we can once again use less conventional functions to build queries that
are capable of exfiltrating data. In this case, the SQL function that we are
interested in is the <pre class="prettyprint inline">ASCII()</pre> function.
This converts a single string character to its ASCII code point, and can be used
to exfiltrate string data from numeric injection points.


At this point, we have a function to turn a single character into a number, but
we still need a way to isolate individual characters from a string. As with many
languages, SQL has a <pre class="prettyprint inline">SUBSTRING()</pre> function
which we can use.


Inner SELECTS
---

Compared to everything else, this is only a tiny note, but in most forms of SQL,
inner SELECT statements (Also known as subselects), are valid. As a fairly useless
 example,

```SQL
SELECT (SELECT (SELECT user, passwd FROM users))
```

is perfectly valid, if useless syntax.


Using this subselect method, we can begin building a payload for this injection
point. If we input '(SELECT ASCII("a"))', we will get back the same record as if
we had used 97 for our input. This is the basis of numeric SQL injection. In
addition to only being able to exfiltrate a single character at a time, numeric
injection often requires you to map out large portions of the website, in order
to figure out what your query is actually returning.


To the Exploitation
---

Now, ordinarily, this query dumps all the columns of the database, so there's
really no point in recovering that. However, let's pretend that there's a generic
"accounts" table sitting on the same database, with an id, username, and password
column. Because we are trying to demonstrate an attack technique, not to exploit
a realistic system, let's pretend that the passwords are unencrypted.


Now to successfully utilize numeric SQL injection, we need to get down to a single
character of a single record. For the record part, we have the LIMIT verb, with two
parameters, in the form

```SQL
SELECT * FROM table LIMIT <offset>,<count>
```

This means that if we do <pre class="prettyprint inline">SELECT * FROM TABLE LIMIT 0,1</pre>
, it will return the very first record from the table (No offset, one
record). Similarly, if we run  
<pre class="prettyprint inline">SELECT * FROM TABLE LIMIT 10,1</pre>, we will get
back the 10th record (Offset 10, one record).


To get from a single record to a single record, we can use the SUBSTRING function.
At this point, this makes our injection payload


```SQL
ASCII(SUBSTRING(<SELECT statement>, <offset>, 1))
```


To test this payload, we can use test strings as a replacement for the SELECT
statement. Placing the string "Test_String" as a placeholder for the SELECT statement,
we create the injection string


```SQL
ASCII(SUBSTRING("Test_String", 1, 1))
```


From here, exploitation becomes a matter of writing this out in a script to assist
in mapping out the website layout and exfiltrating database contents. Because this
is an overview of techniques rather than a demonstration, I'm not going to actually
write this out, but you should get the idea.
