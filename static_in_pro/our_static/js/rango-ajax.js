
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/page/', {image_id : catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});