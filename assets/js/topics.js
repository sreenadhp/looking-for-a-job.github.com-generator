$(document).ready(function(){
    function search() {
        $("#your-repos-filter").trigger("keyup");
    }
    $('#tags').tagsInput({
       'height':'50px',
       'width':'300px',
       'interactive':true,
       'defaultText':'add a tag',
       'onAddTag':search,
       'onRemoveTag':search,
       'onChange' : search,
       'delimiter': [',',';'],   // Or a string with a single delimiter. Ex: ';'
       'removeWithBackspace' : true,
       'minChars' : 0,
       'maxChars' : 0, // if not provided there is no limit
       'placeholderColor' : '#666666'
    });

    $("a.topic-tag").click(function(){
        var tag = $(this).html();
        if ($('#tags').tagExist(tag)) {
            $('#tags').removeTag(tag);
        } else {
            $('#tags').addTag(tag);
        }
    });
});
