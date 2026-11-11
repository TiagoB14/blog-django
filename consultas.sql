-- 1. Todos os posts, do mais recente para o mais antigo
SELECT *
FROM blog_post
ORDER BY pub_date DESC;

-- 2. Todos os comentários de um post (post de id 1)
SELECT *
FROM blog_comment
WHERE post_id = 1;

-- 3. Comentários do post 1 (sem post_id), com título e data do post
SELECT c.id,
       c.text,
       c.pub_date,
       c.author_id,
       p.title,
       p.pub_date AS post_date
FROM blog_comment AS c
INNER JOIN blog_post AS p ON p.id = c.post_id
WHERE c.post_id = 1;

-- 4. Posts de uma categoria (categoria de id 1), com colunas das duas tabelas
SELECT cat.id AS category_id,
       cat.name,
       cat.description,
       p.id AS post_id,
       p.title,
       p.content,
       p.pub_date
FROM blog_category AS cat
INNER JOIN blog_post_categories AS pc ON pc.category_id = cat.id
INNER JOIN blog_post AS p ON p.id = pc.post_id
WHERE cat.id = 1;

-- 5. Categorias com dois ou mais posts
SELECT cat.id,
       cat.name,
       cat.description,
       COUNT(pc.post_id) AS num_posts
FROM blog_category AS cat
INNER JOIN blog_post_categories AS pc ON pc.category_id = cat.id
GROUP BY cat.id, cat.name, cat.description
HAVING COUNT(pc.post_id) >= 2;
