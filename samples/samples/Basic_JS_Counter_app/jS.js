total = 0
nums = 0
entered = ''

make_form()
formButton = document.querySelector("#input")


formButton.addEventListener("click", (e) => {

    if (document.querySelector("input") == null) {
        clear_page()
        make_form()
    }

})

function clear_page() {
    all = document.querySelectorAll("main *")
    for (i = 0; i < all.length; i++) {
        all[i].remove()
    }
}



function make_form() {
    main = document.querySelector("main")


    input = document.createElement("input")
    lable = document.createElement("lable")
    lable.textContent = "Input Number:"


    lable.setAttribute("for", "text")

    input.setAttribute("type", "text")
    input.setAttribute("name", "text")

    let button = document.createElement("button")
    button.textContent = "Save Number"
    button.classList.add("special")
    button.setAttribute("type", "button")
    button.addEventListener("click", event => {
        if (checknum()) {

            number = 0 + parseInt(checknum())
            total += number
            entered += "\r\n" + checknum()
            nums += 1
        }
    })

    holder = document.createElement("form")
    holder.appendChild(lable)
    holder.appendChild(input)
    holder.appendChild(button)


    main.appendChild(holder)


}


home = document.querySelector("#home")

home.addEventListener("click", create_home)




function create_home() {

    if (document.querySelector("h1") == null) {
        clear_page()
        main = document.querySelector("main")
        header = document.createElement("h1")
        header.textContent = "Home page"
        p = document.createElement("p")
        p.textContent = "hello. Welcome to my home page"
        main.appendChild(header)
        main.appendChild(p)
    }

}



moder = document.querySelector("#mode")

moder.addEventListener("click", mode_swap)

function mode_swap(event) {
    if (event.target.textContent === "Light Mode") {
        event.target.textContent = "Dark Mode"
        root = document.querySelector(":root")
        root.style.setProperty("--background", "#fff6e9")
        root.style.setProperty("--accents", "#df758c")
        root.style.setProperty("--text-main", "#683b3b")
    } else {
        event.target.textContent = "Light Mode"
        root.style.setProperty("--background", "#24141e")
        root.style.setProperty("--accents", "#940b29")
        root.style.setProperty("--text-main", "#d2e7ff")
    }

}




function checknum(event) {
    let input = document.querySelector("input")

    if (input) {
        if (isNaN(input.value)) {

            input.style.setProperty("color", "red")

            if (document.querySelector("main p") == null) {
                let main = document.querySelector("main")
                let p = document.createElement("p")
                p.textContent = "Must be a number!"
                main.prepend(p)
            }


        } else if (isNaN(input.value) == false) {
            if (document.querySelector("main p")) {
                document.querySelector("main p").remove()
            }

            input.style.setProperty("color", "#24141e")
            return input.value
        }
    }

}

document.addEventListener("keydown", checknum)


let totalPage = document.querySelector("#total")



totalPage.addEventListener("click", e => {
    clear_page()
    let main = document.querySelector("main")

    let p = document.createElement("p")
    p.textContent = `Your have enter ${nums} numbers \n
The numbers you have entered are:${entered} \n
Your total is: ${total}`

    main.append(p)
})