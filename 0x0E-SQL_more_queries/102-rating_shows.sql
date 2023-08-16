-- The query is designed to calculate the total rating for each TV show. 
-- by joining the tv_shows table with the tv_show_ratings table using a left join.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS "rating" FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY SUM(tv_show_ratings.rate) DESC
;
