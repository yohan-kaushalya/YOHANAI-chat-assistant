
if (!document.getElementById('bg-canvas')) {
    const canvas = document.createElement('canvas');
    canvas.id = 'bg-canvas';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    
    const nodes = [];
    for (let i = 0; i < 45; i++) {
        nodes.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 1.2,
            vy: (Math.random() - 0.5) * 1.2
        });
    }

    function draw() {
        ctx.clearRect(0, 0, width, height);

     
        ctx.strokeStyle = "rgba(0, 242, 254, 0.05)";
        ctx.lineWidth = 1;
        for (let x = 0; x < width; x += 40) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }

        for (let i = 0; i < nodes.length; i++) {
            let p1 = nodes[i];
            p1.x += p1.vx;
            p1.y += p1.vy;

            if (p1.x < 0 || p1.x > width) p1.vx *= -1;
            if (p1.y < 0 || p1.y > height) p1.vy *= -1;

            ctx.fillStyle = "#00f2fe";
            ctx.beginPath();
            ctx.arc(p1.x, p1.y, 2, 0, Math.PI * 2);
            ctx.fill();

            for (let j = i + 1; j < nodes.length; j++) {
                let p2 = nodes[j];
                let dist = Math.hypot(p1.x - p2.x, p1.y - p2.y);
                if (dist < 130) {
                    ctx.strokeStyle = `rgba(0, 242, 254, ${1 - dist / 130})`;
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(draw);
    }
    draw();
}