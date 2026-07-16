/* Education accordion: one card open at a time, synchronized with global language */
(function(){
  function labels(){
    const en=document.documentElement.lang==='en';
    return {closed:en?'Details':'Détails',open:en?'Collapse':'Réduire'};
  }

  function refreshLabels(){
    const copy=labels();
    document.querySelectorAll('[data-education-accordion] [data-edu-card]').forEach((card)=>{
      const label=card.querySelector('.education-toggle-label');
      if(label) label.textContent=card.classList.contains('is-open')?copy.open:copy.closed;
    });
  }

  function initEducationAccordion(){
    document.querySelectorAll('[data-education-accordion]').forEach((timeline)=>{
      const cards=[...timeline.querySelectorAll('[data-edu-card]')];
      cards.forEach((card)=>{
        const button=card.querySelector('.education-summary');
        const details=card.querySelector('.education-details');
        const label=card.querySelector('.education-toggle-label');
        if(!button||!details)return;
        button.addEventListener('click',()=>{
          const opening=!card.classList.contains('is-open');
          const copy=labels();
          cards.forEach((other)=>{
            other.classList.remove('is-open');
            const ob=other.querySelector('.education-summary');
            const od=other.querySelector('.education-details');
            const ol=other.querySelector('.education-toggle-label');
            if(ob)ob.setAttribute('aria-expanded','false');
            if(od)od.hidden=true;
            if(ol)ol.textContent=copy.closed;
          });
          if(opening){
            card.classList.add('is-open');
            button.setAttribute('aria-expanded','true');
            details.hidden=false;
            if(label)label.textContent=copy.open;
          }
          timeline.classList.toggle('has-open',opening);
        });
      });
    });
    refreshLabels();
  }

  window.addEventListener('portfolio:languagechange',refreshLabels);
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initEducationAccordion);else initEducationAccordion();
})();
