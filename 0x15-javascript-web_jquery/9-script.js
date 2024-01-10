$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: (result)=>{
    $('DIV#hello').text(result.hello)
  }
});
