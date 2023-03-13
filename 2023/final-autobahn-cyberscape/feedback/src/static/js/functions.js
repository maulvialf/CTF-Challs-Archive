function loadComments(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            document.getElementById('comments').innerHTML = '';
            var result = this.responseText;
            var results = JSON.parse(result);

            results.forEach((comment)=>
            {
                var node = document.createElement("div");
                var name = document.createElement("H5");
                var date = document.createElement("H6");
                var message = document.createElement("P");

                node.className = 'card-body';
                name.className = 'card-title';
                date.className = 'card-subtitle text-muted';

                name.innerHTML = comment.user;
                date.innerHTML = comment.date;
                message.innerHTML = comment.comment;

                node.appendChild(name);
                node.appendChild(date);
                node.appendChild(message);

                document.getElementById('comments').appendChild(node);
            });
        }
    }
    xhttp.open("GET", "/query", true);
    xhttp.send();
}


function insertComment(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var result = this.responseText;
            console.log(result);
            loadComments();
        } 
    }
    
    var name = document.getElementById('name').value.replace("\\", "").replace("\"", "\\\"").replace(/\n/g, " ");
    var message = document.getElementById('message').value.replace("\"", "\\\"").replace(/\n/g, " ");

    xhttp.open("POST", "/insert", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send('{"name":"'+name+'", "message":"'+message+'"}');
}

