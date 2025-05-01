import { expect, test } from "vitest";
import { render } from "@testing-library/svelte";
import App from "./App.svelte";

test('Overall Render', async () => {
  render(App);
});

test("Test for article display", () => {
  const articles = [
    {
      multimedia: {
        default: { url: "test_img.png" },
        caption: "This is img caption"
      },
      headline: { main: "Title" },
      snippet: "This is snippet of article",
      byline: { original: "By Author" },
      pub_date: "2025-05-01T12:00:00Z",
      web_url: "article_link.com"
    }
  ]

  const { getByText } = render(App, { props: { articles: articles } })

  expect(getByText("Title")).toBeTruthy()
  expect(getByText("This is snippet of article")).toBeTruthy()
  expect(getByText("By Author")).toBeTruthy()
  expect(getByText("Published on: 5/1/2025")).toBeTruthy()
})


