import kue from 'kue';

function createPushNotificationsJobs (jobs, queue){
    if(!Array.isArray(jobs)) {
	throw(new Error('Jobs is not an array'));
    }
    jobs.forEach(function(item) {
	const job = queue.create('push_notification_code_3', item);

	job.save(
	    function (error) {
		if (!error) {
		    console.log(`Notification job created: ${job.id}`);
		}
	    })

	job.on('complete', (result) => {
	    console.log(`Notification job ${job.id} completed`);
	})

	job.on('failed', (err) => {
	    console.log(`Notification job ${job.id} failed: ${err}`);
	})
	job.on('progress', (progress, data) => {
	    console.log(`Notification job ${job.id} ${progress}% complete`);
	})
    })
}

module.exports = createPushNotificationsJobs;
