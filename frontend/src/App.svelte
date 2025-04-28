<script lang="ts">
  import { onMount } from 'svelte';
  import nytLogo from './assets/nyt-logo.png'; // Added missing nytLogo import
  import svelteLogo from './assets/svelte.svg';
  import viteLogo from '/vite.svg';
  import Counter from './lib/Counter.svelte';

  let apiKey: string = '';
  let articles: any[] = []; // Array to store articles
  let currentTime: string = '';
  
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
      // First fetch the API key
      const keyRes = await fetch('/api/key');
      if (!keyRes.ok) {
        throw new Error(`HTTP error! status: ${keyRes.status}`);
      }
      const keyData = await keyRes.json();
      apiKey = keyData.apiKey;
      
      // Then fetch the articles
      const articlesRes = await fetch('/api/articles');
      if (!articlesRes.ok) {
        throw new Error(`HTTP error! status: ${articlesRes.status}`);
      }
      const articlesData = await articlesRes.json();
      articles = articlesData.response?.docs || [];
      console.log("Articles:", articles); // Log the articles to the console for debugging
      currentTime = new Date().toISOString();
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
  <article>
    <h2>Article 1</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Amet consectetur
      adipiscing elit quisque faucibus ex sapien. Quisque faucibus ex sapien
      vitae pellentesque sem placerat. Vitae pellentesque sem placerat in id
      cursus mi.
    </p>
    <a
      title="Keith Weller/USDA, Public domain, via Wikimedia Commons"
      href="https://commons.wikimedia.org/wiki/File:Cow_female_black_white.jpg"
    >
      <img
        width="512"
        alt="Black White cow in green grass field in farm (livestock)"
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Cow_female_black_white.jpg/512px-Cow_female_black_white.jpg?20230829033145"
      />
    </a>
    <figcaption>
      <em>Keith Weller/USDA, Public domain, via Wikimedia Commons</em>
    </figcaption>
  </article>
  <article>
    <h2>Article 2</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet
      consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque
      faucibus ex sapien vitae pellentesque.
    </p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet
      consectetur adipiscing elit quisque faucibus.
    </p>
  </article>
  <article>
    <h2>Article 3</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet
      consectetur adipiscing elit quisque faucibus.
    </p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet
      consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque
      faucibus ex sapien vitae pellentesque.
    </p>
  </article>
  <article>
    <h2>Article 4</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet
      consectetur adipiscing elit quisque faucibus.
    </p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet
      consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque
      faucibus ex sapien vitae pellentesque.
    </p>
    <p>Lorem ipsum dolor sit amet consectetur adipiscing elit.</p>
  </article>
  <article>
    <h2>Article 5</h2>
    <p>Lorem ipsum dolor sit amet consectetur adipiscing elit.</p>
    <!-- image of HTML5 validator pass  -->
    <img src="/images/valid-html.png" alt="Valid HTML5" />
  </article>
  <article>
    <h2>Article 6</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet
      consectetur adipiscing elit quisque faucibus.
    </p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet
      consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque
      faucibus ex sapien vitae pellentesque.
    </p>
  </article>
  <article>
    <h2>Article 7</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet
      consectetur adipiscing elit quisque faucibus.
    </p>
    <p>
      Lorem ipsum dolor sit amet consectetur adipiscing elit. Sit amet
      consectetur adipiscing elit quisque faucibus ex. Adipiscing elit quisque
      faucibus ex sapien vitae pellentesque.
    </p>
    <p>Lorem ipsum dolor sit amet consectetur adipiscing elit.</p>
  </article>
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
