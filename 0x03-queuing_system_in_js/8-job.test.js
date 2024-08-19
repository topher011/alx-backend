import createPushNotificationsJobs from './8-job';
import { expect } from 'chai';
import kue from 'kue';

describe('createPushNotificationsJobs', function () {
    let queue;

    beforeEach(function () {
	queue = kue.createQueue();
	queue.testMode.enter();
    })

    afterEach(function(done) {
	queue.testMode.exit();
	done();
    })

    after(function () {
	queue.testMode.exit();
    })

    it('display a error message if jobs is not an array', function() {
	expect(() => {
	    createPushNotificationsJobs({}, queue)
	}).to.throw('Jobs is not an array');
    })

    it('create two new jobs to the queue', function() {
	const jobs = [
	    { data: { message: 'job1' } },
	    { data: { message: 'job2' } },
	    { data: { message: 'job3' } }
	];
	createPushNotificationsJobs(jobs, queue);
	expect(queue.testMode.jobs.length).to.equal(jobs.length);

	queue.testMode.jobs.forEach((job, index) => {
	    expect(job.type).to.equal('push_notification_code_3');
	    expect(job.data).to.deep.equal(jobs[index]);
	});
    })
})
