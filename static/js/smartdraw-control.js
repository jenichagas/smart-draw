import Alpine from "https://unpkg.com/alpinejs?module";

window.Alpine = Alpine;

document.addEventListener("alpine:init", () => {
    Alpine.data("smartDraw", () => ({
        winner: false,

        init() {
            document.body.addEventListener("htmx:afterRequest", (evt) => {
                const form = evt.target;
                if (form?.getAttribute("hx-post") == "/smartdraw/add") {
                    const input = form.querySelector('input[name="name"]');
                if (input) {
                        input.value = "";
                    }
                }

                if (evt.detail.requestConfig?.path === "/smartdraw/draw") {
                    this.winner = true; 
                }
            });

        },



    }));
});

Alpine.start();
