<script lang="ts">
  import { onMount } from 'svelte';
  import nytLogo from './assets/nyt-logo.png'; // Added missing nytLogo import

  let articles: any[] = []; // Array to store articles

  // Date formatting for header
  const date = new Date();
  const options = {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  };
  const date_display = date.toLocaleDateString("en-US", options);
  
  onMount(async () => {
    try {
      
      const articlesRes = await fetch('/api/articles');
      if (!articlesRes.ok) {
        throw new Error(`HTTP error! status: ${articlesRes.status}`);
      }
      const articlesData = await articlesRes.json();
      articles = articlesData.response?.docs || [];
      console.log("Articles JSON:", JSON.stringify(articles, null, 2)); // Log the articles JSON to the console for debugging
    } catch (error) {
      console.error('Failed to fetch data:', error);
    }
  });
</script>

<header>
  <div class="header-container">
    <!-- logo image and dynamic date -->
    <img src={nytLogo} alt="The New York Times" />
    <div id="current-date">{date_display}</div>
  </div>
  <nav class="main-nav">
    <ul>
      <!-- list of potential pages -->
      <li class="nav-item"><a href="#">U.S.</a></li>
      <li class="nav-item"><a href="#">World</a></li>
      <li class="nav-item"><a href="#">Business</a></li>
      <li class="nav-item"><a href="#">Arts</a></li>
      <li class="nav-item"><a href="#">Lifestyle</a></li>
      <li class="nav-item"><a href="#">Opinion</a></li>
      <li class="nav-item"><a href="#">Audio</a></li>
      <li class="nav-item"><a href="#">Games</a></li>
      <li class="nav-item"><a href="#">Cooking</a></li>
      <li class="nav-item"><a href="#">Wirecutter</a></li>
      <li class="nav-item"><a href="#">Atlantic</a></li>
    </ul>
  </nav>
</header>
<hr />
<hr />
<main>
  <!-- main content area displayed as dynamic grid layout -->
  {#each articles as article}
    <article class="article-card">
      <h2>{article.headline.main}</h2>
      <p>{article.snippet}</p>
      <p class="article-url"><a href={article.web_url} target="_blank">{article.web_url}</a></p>
      <p>Published on: {new Date(article.pub_date).toLocaleDateString()}</p>
      <a href={article.web_url} target="_blank" class="read-more">Read more</a>
    </article>
  {/each}
</main>
<footer>
  <!-- footer for additonal information -->
  <div class="footer-content">
    <p>
      <!-- CSS validator pass -->
      <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img
          style="border:0;width:88px;height:31px"
          src="https://jigsaw.w3.org/css-validator/images/vcss"
          alt="Valid CSS!"
        />
      </a>
    </p>
    <p>&copy; 2024 The New York Times</p>
    <p>Zoey Vo</p>
    <p>Text generated with:</p>
    <a href="https://loremipsum.io/generator/" target="_blank"
      >Lorem Ipsum Generator</a
    >
  </div>
</footer>

<style>
</style>
