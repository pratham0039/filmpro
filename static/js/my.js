document.addEventListener('DOMContentLoaded', function () {


	document.querySelector('#btn-one').addEventListener('click', function () {
		html2canvas(document.querySelector('#pdf-container')).then((canvas) => {
			let base64image = canvas.toDataURL('image/png');
			
			let pdf = new jsPDF('p', 'px', [500, 1131]);
			pdf.addImage(base64image, 'PNG', 15, 15, 600, 60);
			pdf.save('continuity_sheet.pdf');
		});
	});

});
