const CACHE="menare-v8";
const FILES=["./","index.html","manifest.webmanifest","fonts/SarkarAljazeera-Regular.woff2","fonts/SarkarAljazeera-Bold.woff2","fonts/Amiri-Regular.woff2","fonts/Amiri-Bold.woff2",
 "icons/icon-192.png","icons/icon-512.png","icons/maskable-512.png","icons/apple-touch-icon.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()));});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(n=>n!==CACHE).map(n=>caches.delete(n)))).then(()=>self.clients.claim()));});
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET")return;
  if(e.request.mode==="navigate"){
    e.respondWith(fetch(e.request).then(r=>{const c=r.clone();caches.open(CACHE).then(x=>x.put("index.html",c));return r;}).catch(()=>caches.match("index.html")));
    return;}
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));
});
