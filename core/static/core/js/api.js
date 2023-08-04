$("#buscar").click(function() {
    $.get("https://jsonplaceholder.typicode.com/users",
        function(data) {
            $.each(data.productos, (function(i, item) {
                $("#personas").append("<tr><td>" + item.id + "</td> <td>" +
                    item.name + "</td> <td> <img src ='" + item.username + "'></td> <td>" +
                    item.email + "</td></tr>");
            }));
        });

});