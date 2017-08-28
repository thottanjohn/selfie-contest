jQuery(document).ready(function(){
    "use strict"
    // Comments Reply
    jQuery(".comment-reply-link").on('click',function(e) {
        e.preventDefault();
        jQuery('html,body').animate({
                scrollTop: jQuery(".bt-leavereplay").offset().top
            },
            'slow');
        jQuery('#cancel-comment-reply-link').show();
        var cID = jQuery(this).next().val();
        jQuery('#comment_parent').val(cID);
    });
    jQuery(".comment-reply-link").each(function(){
        jQuery(this).removeAttr('onclick');
    });
    jQuery('#cancel-comment-reply-link').on('click',function(e){
        e.preventDefault();
        jQuery(this).hide();
        jQuery('#comment,#author,#email,#url').val('');
    });
    // Change submit HTML
    jQuery("p.form-submit").each(function () {
        jQuery(this).replaceWith("<div class='col-xs-12 col-sm-12 col-md-12 col-lg-12 text-right'>" + jQuery(this).html() + "</div>");
    });
    // Generals Backgrounds
    jQuery('section,div').each(function(){
        var url = jQuery(this).attr("data-image");
        if(url){
            jQuery(this).css("background-image", "url(" + url + ")");
        }
        var bs = jQuery(this).attr("data-bs");
        if(bs){
            jQuery(this).css("background-size", "" + bs + "");
        }
        var bp = jQuery(this).attr("data-bp");
        if(bp){
            jQuery(this).css("background-attachment", "" + bp + "");
        }
    });
    // Menu
    jQuery('ul li.menu-item').each(function(){
        jQuery(this).addClass('bt-hasdropdown');
    });
    // Newsletter
    jQuery('.bt-formnewsletter .wysija-submit').each(function(){
        jQuery(this).after('<button type="submit"><i class="icon-email2"></i></button>');
    });
    // Home 2
    jQuery('.bt-home.bt-homevtwo.bt-homevalbums.bt-fixed').each(function(){
        jQuery(this).find('.bt-footer').addClass('bt-footerborder');
    });
});