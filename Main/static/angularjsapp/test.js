function checkCredentials(username, password) {
    function setHeader(xhr) {
        // as per HTTP authentication spec [2], credentials must be
        // encoded in base64. Lets use window.btoa [3]
        xhr.setRequestHeader("Authorization", "Basic " +
        btoa(username + ':' + password));
    }

    $.ajax({type: "POST", url: "/api/auth/", beforeSend: setHeader}).
        fail(function (resp) {
            console.log('bad credentials.')
        }).
        done(function (resp) {
            console.log('welcome ' + resp.email)
        });
}

