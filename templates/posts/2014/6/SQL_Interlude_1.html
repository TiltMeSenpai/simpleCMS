<p>So, now we know how to break our application (A lot), but how to we fix it? Luckily, despite being so common, SQL injections are comparatively easy to fix. In short, you have 3 options.</p>
<p><ul>
    <li>Escape</li>
    <li>Encode</li>
    <li>Bind</li>
</ul>
</p>
<p>
<h2>Escape: </h2>
        If you remember, the targeted query looks like:
        <pre class="prettyprint lang-sql">
        SELECT name, number FROM phonebook WHERE user LIKE '*input*';
        </pre> 
        And every single SQL injection so far has included a single quote character (Could actually be a double quote).
        Because of this, the simplest way to fix an SQL injection is to remove all quote characters, but you have to do it right.
        <h3>WRONG</h3>
        <pre class="prettyprint">
        SELECT name, number FROM phonebook WHERE user LIKE '+ re.sub(r'\'', r'\\\'', input)
        </pre>
        Wait, what? That escapes all of the single quote characters, right? Well, kind of. In reality, if an attacker inputs "\'", our regular expression will escape the single quote, but won't touch the backslash. What we end up with is the string "\\'", or a literal backslash followed by a single quote.  If we were to inject \\' UNION SELECT @@version, we would still get succesful injection. The double backslash would be interpreted as a literal backslash at the server level, and the single quote is escaped. This transforms into:
        <pre class="prettyprint">
        SELECT name, number FROM phonebook WHERE user LIKE '\\' UNION @@version;
        </pre>
        In order to properly escape our string, we would have to escape all single quotes, all backslashes, and all encoded variants. Unless we use a readily made library and let someone else worry about the encoding, we would have to catch every possibility. However, escaping is fortunately potentially the least efficient technique

<h2>Encode: </h2>
If you've ever read any article on filter/WAF evasion, you've seen hex sequences used to avoid using single quote characters (Some filters/WAF's will flag them as attempted SQLi). This actually may not be entirely obvious, but we can actually use this to protect ourselves agains SQL injection. In quote-free SQL injection payloads, hex sequences are used in place of string data. Levering this to our advantage, we can hex encode our user inputs to ensure that no malicious input can get through our queries untouched. If we use something like <pre class="prettyprint lang-python inline"> binascii.hexlify(*user input*.encode()) </pre>, we can encode all our user input into hex strings. From here, our query can become
<pre class="prettyprint lang-sql">
SELECT name, number FROM phonebook WHERE user LIKE 0x'+binascii.hexlify(user_input.encode())';
</pre>
and our valid query for finding Mr. O'Malley's phone number ends up looking like
<pre class="prettyprint lang-sql">
SELECT name, number FROM phonebook WHERE name LIKE 0x4d722e204f274d616c6c6579;
</pre>
and despite looking nothing like what we would expect it to, this query does exactly what it advertises (At least on MySQL).
<em>Note: You have to import binascii. Hope you noticed that one.</em>

<h2>Prepare:</h2>
Okay, time to take a break from Python. Why? Python's MySQL api does SQL horribly wrong. The reason light wrappers like TornDB exist is to convert these horrible interfaces into something that's actually sane and usable. However, TornDB is no longer in development, and it doesn't support prepared statements. Because of this, let's look at Java, which actually does SQL reasonably well.
<pre class="prettyprint">
PreparedStatement statement = new PreparedStatement("SELECT name, number FROM phonebook WHERE name LIKE ?");
statement.setString(1, user_input);
ResultSet numbers = statement.execute();
</pre>
Now, we see our code is no longer a one-liner. However, this new format uses an <em>entirely different </em> interface to pass the data. When you use prepared statements, the SQL interface uses a binary protocol to talk to the database, and instead of passing data inside the query, the data is passed alongside the query. It's the difference between "a+b" and "a, b". However, the biggest reason why this is the right way to do things, is if we reuse our PreparedStatement object to execute more queries for phone numbers, we actually will see a performance increase. This is because MySQL will compile and store our prepared statement, leaving space for our input, and the database will be able to optimize our query further than if we had submitted it as a normal string query.
