$.get('https://stefanbohacek.com/hellosalut/?lang=fr', (content) => {
  $('DIV#hello').text(content.hello);
});
