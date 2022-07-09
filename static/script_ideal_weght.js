const btn = document.querySelector('.send__data__btn');

btn.addEventListener('click', function () {
    let user_height = parseInt(document.getElementById("user_height").value);
    let user_hand = parseInt(document.getElementById("user_hand").value);
    let user_age = parseInt(document.getElementById("user_age").value);
    let user_sex = document.getElementById("user_sex").value
    if (isNaN(user_age) || isNaN(user_height) || isNaN(user_hand)) {
        //None
        document.getElementById("user_height").focus();
    }
    else {

        fetch('/app_ideal_weght', {
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST',
            body: JSON.stringify({
                "user_height": user_height,
                "user_hand": user_hand,
                "user_age": user_age,
                "user_sex": user_sex
            })
        })
            .then(function (response) {

                if (response.ok) {
                    response.json()
                        .then(function (response) {
                            //console.log(response);
                            document.getElementById('response').innerHTML = response.response;
                            document.getElementById("response").scrollIntoView();
                        });
                }
                else {
                    throw Error('Something went wrong');
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }
});