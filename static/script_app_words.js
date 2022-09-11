
const btn = document.querySelector('.send__data__btn');

btn.addEventListener('click', function () {
    let some_text = document.getElementById("some_text").value
    if (typeof some_text != 'string' || some_text.length === 0) {
        //None
        document.getElementById("some_text").focus();
    } else {
        fetch('/app_words', {
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST',
            body: JSON.stringify({
                "some_text": some_text,
            })
        }).then(function (response) {
            if (response.ok) {
                response.json().then(function (response) {
                    console.log(response);
                    document.getElementById('sum_all_words').innerHTML = response.response.sum_all_words;
                    document.getElementById('sum_punctuation').innerHTML = response.response.sum_punctuation;
                    document.getElementById('sum_unique_words').innerHTML = response.response.sum_unique_words;
                    document.getElementById('list_one_word').innerHTML = response.response.list_one_word;
                    const div = document.getElementById('dic');
                    document.getElementById('dic').innerHTML = '';
                    response.response.new_list.forEach(function (item, index) {
                        let html = `<li class="list-group-item">Word: <b>'${item.word}'</b> repeats <b>${item.sum}</b> times</li>`;
                        div.insertAdjacentHTML('beforeend', html);
                    })
                });
            } else {
                throw Error('Something went wrong');
            }
        }).catch(function (error) {
            console.log(error);
        });
    }
});