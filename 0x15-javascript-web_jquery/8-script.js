$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (result)=>{
    $.each(result.results, (i, el)=>{
      $('UL#list_movies').append('<li>'+el.title+'</li>')
    })
  }
});
