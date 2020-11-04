document.addEventListener('DOMContentLoaded', () => {
    const elems = document.querySelectorAll('.carousel');
    M.Carousel.init(elems, {
        duration: 1500,
        dist: -58,
        shift: 5,
        padding: 5,
        numVisible: 5,
    });
});