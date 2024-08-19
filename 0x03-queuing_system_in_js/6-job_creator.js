import kue from 'kue';

const push_notification_code = kue.createQueue();
const job_data = {
  phoneNumber: '0798845673',
  message: 'This is the message',
};
let job = push_notification_code.create('push_notification_code',
					job_data).save(function(err) {
    if (!err) {
	console.log(`Notification job created: ${job.id}`);
    } else {
	console.error(`Error creating notification job: ${err}`);
    }
});

job.on('complete', (result) => {
    console.log(`Notification job created: ${job.id}`);
})

job.on('failed', (err) => {
    console.log('Notification job failed');
})
