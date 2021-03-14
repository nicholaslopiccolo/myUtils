process.on('uncaughtException',function(err){
  console.log('error');
  // send Email
  process.exit(1);
})
