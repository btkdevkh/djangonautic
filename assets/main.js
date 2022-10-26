const title = document.querySelector('input[name=title]')
const slug = document.querySelector('input[name=slug]')

if(title) {
  title.addEventListener('keyup', () => {
    slug.value = title.value
      .toString()
      .toLowerCase()
      .trim()
      .replace(/&/g, '-and-')
      .replace(/[\s\W-]+/g, '-')
  })
}
